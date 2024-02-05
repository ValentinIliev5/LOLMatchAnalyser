package lol.analyser.utils;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SequenceWriter;
import com.fasterxml.jackson.databind.node.ArrayNode;
import lol.analyser.model.AccountInfo;
import lol.analyser.model.AccountsHolder;
import lol.analyser.services.AccountService;
import lol.analyser.services.MatchService;
import lombok.*;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

@NoArgsConstructor
@Getter
@Setter
@Builder
public class DataExtractor {

    public void ExtractMatchesIds() throws IOException, InterruptedException {

        MatchService matchService = new MatchService();
        AccountsHolder accountsHolder = new AccountsHolder();

        accountsHolder.initAccounts();
        ArrayList<String> matchIds = new ArrayList<>();
        for (AccountInfo accountInfo : accountsHolder.getAccounts()) {
            System.out.println(accountInfo.getUsername());

            AccountService service = AccountService.builder().accountInfo(accountInfo).build();
            String userPUUID = service.getUserPUUID().replace("\"", "");

            for (int i = 0; i <= 900; i += 100) {
                JsonNode jsonObj = matchService.getMatchesIDs(userPUUID, i);

                ArrayNode arrayNode = (ArrayNode) jsonObj;
                for (JsonNode node : arrayNode) {
                    matchIds.add(node.toString().replace("\"", ""));
                }
            }
            TimeUnit.SECONDS.sleep(15);
        }

        BufferedWriter writer = new BufferedWriter(new FileWriter("MATCHES_IDS.txt"));
        for (String matchID : matchIds) {
            writer.write(matchID);
            writer.newLine();
        }
        writer.close();
    }
    public void extractMatchesDetails(File file){
        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {

            String line;
            int counter = 4894;
            ObjectMapper objectMapper = new ObjectMapper();
            MatchService matchService = new MatchService();
            File matchesFile = new File("matchesData.json");

            SequenceWriter sequenceWriter = objectMapper.writer().writeValuesAsArray(matchesFile);

            while ((line = reader.readLine()) != null) {

                JsonNode matchJson = matchService.readMatchData(line);

                sequenceWriter.write(matchJson);

                if(counter%11==0)
                {
                    TimeUnit.SECONDS.sleep(15);
                }
                counter++;
                System.out.println(line+ " " + counter +" of " + 12677);
            }
            sequenceWriter.close();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
