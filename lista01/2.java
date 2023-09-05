import java.util.Scanner;

public class CrapsGame {
    public static void main(String[] args) {
        playGame();
    }

    public static void playGame() {
        Scanner scanner = new Scanner(System.in);
        String input;

        do {
            System.out.println("Pressione enter para rolar o dado...");
            scanner.nextLine();

            int dice1 = (int) (Math.random() * 6) + 1;
            int dice2 = (int) (Math.random() * 6) + 1;
            int sum = dice1 + dice2;

            System.out.println("Você rolou: " + dice1 + " + " + dice2 + " = " + sum);

            if (sum == 7 || sum == 11) {
                System.out.println("Venceu!");
            } else if (sum == 2 || sum == 3 || sum == 12) {
                System.out.println("Perdeu!");
            } else {
                int point = sum;
                System.out.println("Point is set to " + point);
                
                boolean gameFinished = false;
                while (!gameFinished) {
                    System.out.println("Pressione enter para rolar o dado...");
                    scanner.nextLine();
                    
                    dice1 = (int) (Math.random() * 6) + 1;
                    dice2 = (int) (Math.random() * 6) + 1;
                    sum = dice1 + dice2;
                    
                    System.out.println("Você rolou: " + dice1 + " + " + dice2 + " = " + sum);
                    
                    if (sum == 7) {
                        System.out.println("Perdeu!");
                        gameFinished = true;
                    } else if (sum == point) {
                        System.out.println("Venceu!");
                        gameFinished = true;
                    }
                }
            }

            System.out.println("Deseja jogar novamente?(y/n)");
            input = scanner.nextLine();
        } while (input.equalsIgnoreCase("y"));

        System.out.println("Obrigado por jogar!");
        scanner.close();
    }
}
