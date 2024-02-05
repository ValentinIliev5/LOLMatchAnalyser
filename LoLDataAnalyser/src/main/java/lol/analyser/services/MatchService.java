package lol.analyser.services;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
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
public class MatchService {

    @Builder.Default
    private String findMatchesID =
            "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/";
    @Builder.Default
    private String getMatchDetails =
            "https://europe.api.riotgames.com/lol/match/v5/matches/";

    private URL formAllMatchesURL(String userPUUID,int startNumber) throws MalformedURLException {
        String url = findMatchesID+userPUUID+"/ids?start="+startNumber+"&count=100&api_key="+ ApiKey.getKey();
        return new URL(url);
    }
    private URL formGetMatchDetailsURL(String matchID) throws MalformedURLException {
        String url = getMatchDetails+matchID+"?api_key="+ApiKey.getKey();
        return new URL(url);
    }

    public JsonNode getMatchesIDs(String userPUUID,int startNumber) throws IOException {
       HttpURLConnection connection = (HttpURLConnection) formAllMatchesURL(userPUUID,startNumber).openConnection();
        return getJsonNode(connection);
    }


    public JsonNode readMatchData(String matchID) throws IOException {
        HttpURLConnection connection = (HttpURLConnection) formGetMatchDetailsURL(matchID).openConnection();
        return getJsonNode(connection);
    }
    private static JsonNode getJsonNode(HttpURLConnection connection) throws IOException {
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

}
