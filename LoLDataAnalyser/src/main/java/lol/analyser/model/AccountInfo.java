package lol.analyser.model;
import lombok.*;

@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
public class AccountInfo {
    @Builder.Default
    private String username = "Value";
    @Builder.Default
    private String tag = "KYPBN";

}
