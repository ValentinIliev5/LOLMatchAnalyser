package lol.analyser;

import com.fasterxml.jackson.databind.JsonNode;
import lol.analyser.services.MatchService;
import lol.analyser.utils.DataExtractor;

import java.io.*;
import java.util.concurrent.TimeUnit;

public class Main {

    public static void main(String[] args) throws IOException, InterruptedException {
        DataExtractor dataExtractor = DataExtractor.builder().build();
        File file = new File("MATCHES_IDS2.txt");
        if(file.exists())
        {
            dataExtractor.extractMatchesDetails(file);
        }
        else {
            dataExtractor.ExtractMatchesIds();
        }
    }
}
