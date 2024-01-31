package lol.analyser;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ArrayNode;
import lol.analyser.model.AccountInfo;
import lol.analyser.model.AccountsHolder;
import lol.analyser.services.AccountService;
import lol.analyser.services.MatchService;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class Main {

    public static void main(String[] args) throws IOException, InterruptedException {

        AccountsHolder accountsHolder = new AccountsHolder();
        accountsHolder.initAccounts();
        ArrayList<String> matchIds = new ArrayList<>();
        for(AccountInfo accountInfo : accountsHolder.getAccounts())
        {
            System.out.println(accountInfo.getUsername());

            AccountService service = AccountService.builder().accountInfo(accountInfo).build();
            String userPUUID = service.getUserPUUID().replace("\"","");
            MatchService matchService = new MatchService();
            for(int i=0;i<=900;i+=100)
            {
                JsonNode jsonObj = matchService.getMatchesIDs(userPUUID,i);
                ArrayNode arrayNode = (ArrayNode) jsonObj;
                for(JsonNode node : arrayNode)
                {
                    matchIds.add(node.toString().replace("\"",""));
                }
            }
            TimeUnit.SECONDS.sleep(5);
        }
    }
}
