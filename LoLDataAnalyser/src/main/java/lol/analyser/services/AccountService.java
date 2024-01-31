package lol.analyser.services;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import lol.analyser.model.AccountInfo;
import lol.analyser.ApiKey;
import lombok.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

@Builder
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class AccountService {

    private AccountInfo accountInfo;
    @Builder.Default
    private String api_string ="https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/";

    private URL getApiUrl() throws MalformedURLException {
        api_string = api_string+this.accountInfo.getUsername() + "/"+this.accountInfo.getTag()+ "?api_key=" + ApiKey.getKey();
        return new URL(api_string);
    }
    private JsonNode getUserData() throws IOException {
        HttpURLConnection connection = (HttpURLConnection)getApiUrl().openConnection();
        connection.setRequestMethod("GET");

        int responseCode = connection.getResponseCode();
        JsonNode jsonNode = null;

        if (responseCode == HttpURLConnection.HTTP_OK)
        {
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder response = new StringBuilder();
            String line;

            while ((line = reader.readLine()) != null) {
                response.append(line);
            }

            reader.close();

            ObjectMapper objectMapper = new ObjectMapper();
            jsonNode = objectMapper.readTree(response.toString());

            //System.out.println("JSON Response:\n" + jsonNode);
        }
        else {
            System.out.println("Failed to retrieve data. Response Code: " + responseCode);
        }

        connection.disconnect();
        return jsonNode;
    }

    public String getUserPUUID() throws IOException {
        return this.getUserData().get("puuid").toString();
    }


}
