import java.util.Scanner;
import java.util.Random;

public class Guessing_Game {
    public static void main(String[] args) {
        boolean guessed = false;

        Random random = new Random();
        Scanner playerGuess = new Scanner(System.in);

        int guess = random.nextInt(1, 100);

        while (guessed == false){
            System.out.print("Guess a # 1-100: ");
            int readGuess = playerGuess.nextInt();

            if(readGuess == guess) {
                System.out.println("Bingo!");
                guessed = true;
            }
            else if(readGuess > guess) {
                System.out.println("Lower");
            }
            else if (readGuess < guess) {
                System.out.println("Higher");
            }
        }
        playerGuess.close();
    }
}
