package lol.analyser.model;

import lombok.*;

import java.util.ArrayList;

@Builder
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class AccountsHolder {

    private ArrayList<AccountInfo> accounts = new ArrayList<>();

    public void initAccounts()
    {
        this.accounts.add(AccountInfo.builder().build());
        this.accounts.add(new AccountInfo("Nub4e","EUNE"));
        this.accounts.add(new AccountInfo("Azmanis","EUNE"));
        this.accounts.add(new AccountInfo("Truthseeker","VEN"));
        this.accounts.add(new AccountInfo("Vladimus","1337"));
        this.accounts.add(new AccountInfo("PistonKosiarz","BOSS"));
        this.accounts.add(new AccountInfo("ok6og","EUNE"));
        this.accounts.add(new AccountInfo("Overlord474","EUNE"));
        this.accounts.add(new AccountInfo("Trolge","EUNE"));
        this.accounts.add(new AccountInfo("Lisara","AYAYA"));
        this.accounts.add(new AccountInfo("Josyuker","Joker"));
        this.accounts.add(new AccountInfo("Killer","BQG1"));
        this.accounts.add(new AccountInfo("Veskin","2121"));
        this.accounts.add(new AccountInfo("NoWardJustBard","2106"));
    }
    public void addAccount(AccountInfo accountInfo){
        this.accounts.add(accountInfo);
    }
}
