import java.util.Scanner;

public class BattleshipGame {
  private static final int BOARD_SIZE = 5;
  private static final char EMPTY = '-';
  private static final char SHIP = '@';
  private static final char HIT = 'X';
  private static final char MISS = 'O';

  private char[][] player1Board;
  private char[][] player2Board;
  private char[][] player1History;
  private char[][] player2History;

  public BattleshipGame() {
    player1Board = new char[BOARD_SIZE][BOARD_SIZE];
    player2Board = new char[BOARD_SIZE][BOARD_SIZE];
    player1History = new char[BOARD_SIZE][BOARD_SIZE];
    player2History = new char[BOARD_SIZE][BOARD_SIZE];

    initializeBoard(player1Board);
    initializeBoard(player2Board);
    initializeBoard(player1History);
    initializeBoard(player2History);
  }

  private void initializeBoard(char[][] board) {
    for (int i = 0; i < BOARD_SIZE; i++) {
      for (int j = 0; j < BOARD_SIZE; j++) {
        board[i][j] = EMPTY;
      }
    }
  }

  private void printBoard(char[][] board) {
    for (int i = 0; i < BOARD_SIZE; i++) {
      for (int j = 0; j < BOARD_SIZE; j++) {
        System.out.print(board[i][j] + " ");
      }
      System.out.println();
    }
  }

  private boolean isValidCoordinate(int row, int col) {
    return row >= 0 && row < BOARD_SIZE && col >= 0 && col < BOARD_SIZE;
  }

  private boolean isCoordinateEmpty(char[][] board, int row, int col) {
    return board[row][col] == EMPTY;
  }

  private boolean isCoordinateAlreadyUsed(char[][] board, int row, int col) {
    return board[row][col] != EMPTY;
  }

  private void placeShip(char[][] board, int row, int col) {
    board[row][col] = SHIP;
  }

  private boolean isShipSunk(char[][] board) {
    for (int i = 0; i < BOARD_SIZE; i++) {
      for (int j = 0; j < BOARD_SIZE; j++) {
        if (board[i][j] == SHIP) {
          return false;
        }
      }
    }
    return true;
  }

  private void updateBoard(char[][] board, int row, int col, boolean isHit) {
    if (isHit) {
      board[row][col] = HIT;
    } else {
      board[row][col] = MISS;
    }
  }

  private void playGame() {
    Scanner scanner = new Scanner(System.in);

    System.out.println("Welcome to Battleship!!!");

    // Player 1 input ships
    for (int i = 1; i <= 5; i++) {
      System.out.println("Player 1, enter coordinates for ship " + i + ":");
      int row = scanner.nextInt();
      int col = scanner.nextInt();

      if (!isValidCoordinate(row, col)) {
        System.out.println("Invalid coordinates. Choose different coordinates.");
        i--;
        continue;
      }

      if (isCoordinateAlreadyUsed(player1Board, row, col)) {
        System.out.println("You already have a ship there. Choose different coordinates.");
        i--;
        continue;
      }

      placeShip(player1Board, row, col);
      printBoard(player1Board);
    }

    // Player 2 input ships
    for (int i = 1; i <= 5; i++) {
      System.out.println("Player 2, enter coordinates for ship " + i + ":");
      int row = scanner.nextInt();
      int col = scanner.nextInt();

      if (!isValidCoordinate(row, col)) {
        System.out.println("Invalid coordinates. Choose different coordinates.");
        i--;
        continue;
      }

      if (isCoordinateAlreadyUsed(player2Board, row, col)) {
        System.out.println("You already have a ship there. Choose different coordinates.");
        i--;
        continue;
      }

      placeShip(player2Board, row, col);
      printBoard(player2Board);
    }

    // Game loop
    int currentPlayer = 1;
    while (true) {
      System.out.println("Player " + currentPlayer + ", enter coordinates to fire:");

      int row = scanner.nextInt();
      int col = scanner.nextInt();

      if (!isValidCoordinate(row, col)) {
        System.out.println("Invalid coordinates. Choose different coordinates.");
        continue;
      }

      if (currentPlayer == 1) {
        if (isCoordinateAlreadyUsed(player1History, row, col)) {
          System.out.println("You already fired on this spot. Choose different coordinates.");
          continue;
        }

        if (player2Board[row][col] == SHIP) {
          System.out.println("Player 1 hit Player 2's Ship!!!");
          updateBoard(player2Board, row, col, true);
          updateBoard(player1History, row, col, true);
        } else {
          System.out.println("Player 1 MISSED!");
          updateBoard(player1History, row, col, false);
        }

        printBoard(player1History);

        if (isShipSunk(player2Board)) {
          System.out.println("Player 1 WINS! You sunk all of your opponent's ships!");
          printBoard(player1Board);
          printBoard(player2Board);
          break;
        }

        currentPlayer = 2;
      } else {
        if (isCoordinateAlreadyUsed(player2History, row, col)) {
          System.out.println("You already fired on this spot. Choose different coordinates.");
          continue;
        }

        if (player1Board[row][col] == SHIP) {
          System.out.println("Player 2 hit Player 1's Ship!!!");
          updateBoard(player1Board, row, col, true);
          updateBoard(player2History, row, col, true);
        } else {
          System.out.println("Player 2 MISSED!");
          updateBoard(player2History, row, col, false);
        }

        printBoard(player2History);

        if (isShipSunk(player1Board)) {
          System.out.println("Player 2 WINS! You sunk all of your opponent's ships!");
          printBoard(player2Board);
          printBoard(player1Board);
          break;
        }

        currentPlayer = 1;
      }
    }

    scanner.close();
  }

  public static void main(String[] args) {
    BattleshipGame game = new BattleshipGame();
    game.playGame();
  }
}