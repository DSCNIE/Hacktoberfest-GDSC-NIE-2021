package MinesweeperGame;


//Following is the implementation of Minesweeper.



import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.*;

public class Minesweeper extends JFrame implements ActionListener, MouseListener{


    JFrame frame = new JFrame();               
    JButton reset = new JButton("Reset");       //Reset Button as a side.
    JButton giveUp = new JButton("Give Up");    //Similarly, give up button.  
    JPanel ButtonPanel = new JPanel();       
    Container grid = new Container();           
    int[][] counts;                             //integer array to store counts of each cell. Used as a back-end for comparisons.
    JButton[][] buttons;                        //Buttons array to use as a front end for the game.
    int size,diff;                              
    final int MINE = 10;                        

    /**
    @param size determines the size of the board
    */

    public Minesweeper(int size){
     super("Minesweeper");                       

     this.size = size;   
     counts = new int[size][size];
     buttons = new JButton[size][size];  

     frame.setSize(900,900);                       
     frame.setLayout(new BorderLayout());           
     frame.add(ButtonPanel,BorderLayout.SOUTH);     
     reset.addActionListener(this);                 
     giveUp.addActionListener(this);                


     grid.setLayout(new GridLayout(size,size));    

     for(int a = 0; a < buttons.length; a++)
     {
         for(int b = 0; b < buttons[0].length; b++)
         {
             buttons[a][b] = new JButton();            
             buttons[a][b].addActionListener(this);     
             grid.add(buttons[a][b]);                  
         }
     }
     // above initializes each button in the minesweeper board and gives it functionality. 

     ButtonPanel.add(reset);                        
     ButtonPanel.add(giveUp);       // adding buttons to the panel.

     frame.add(grid,BorderLayout.CENTER);   
     createMines(size);                         //calling function to start the game by filling mines.

     frame.setLocationRelativeTo(null);      
     frame.setDefaultCloseOperation(EXIT_ON_CLOSE);     //frame stuff
     frame.setVisible(true);

    }
    /**
     * Function to check whether user has lost the game ( i.e clicked a mine).
     * @param m indicated whether the function has been called when user clicks a mine( m=1)
     * or when he clicks the give up button.(m = any other integer).
     * Shows a dialog box which tells the user that they have lost the game.
     */
    public void takeTheL(int m){

        for(int x = 0; x < size; x++)
        {
            for(int y = 0; y < size; y++)
            {
                if(buttons[x][y].isEnabled())          // when a button has been clicked, it is disabled.
                {
                    if(counts[x][y] != MINE)
                    {
                        buttons[x][y].setText(""+ counts[x][y]);                    
                    }

                    else
                    {
                        buttons[x][y].setText("X");

                    }
                    buttons[x][y].setEnabled(false);
                }
            }
        }
    JOptionPane.showMessageDialog(null, m==1? "You clicked a mine!":"You Gave Up",
                                 "Game Over", JOptionPane.ERROR_MESSAGE);
    } 
    /**
     * Function to check whether user has won or not
     * It performs this by checking whether a cell that is NOT a mine
     * remains to be clicked by the user.
     * (Works because, when a user clicks a button, it is disabled to avoid further moves on the same cell).
     * Function prints a pop-up message congratulating user on victory.
     */

    public void takeTheW() {
       boolean won = true;
       for(int i = 0; i < size; i++)
       {
           for(int j = 0; j < size; j++)
           {
               if(counts[i][j] != MINE && buttons[i][j].isEnabled())
               {
                   won = false;
               }
           }
       }
       if(won) 
       {
            JOptionPane.showMessageDialog(null,"You have won!", "Congratulations!",
                                          JOptionPane.INFORMATION_MESSAGE);
       }   
    }



    @Override
    public void actionPerformed(ActionEvent ae) {
        if(ae.getSource() == reset)              //resets grid
        {
            for(int x = 0; x < size; x++)
            {
                for(int y = 0; y < size; y++)
                {
                    buttons[x][y].setEnabled(true);
                    buttons[x][y].setText("");
                }
            }
            createMines(30);  //triggers a new game.
        }

        else if(ae.getSource() == giveUp)  //user has given up. trigger takeTheL( m!= 1).
        {
                   takeTheL(0); // anything not = 1
        }

        else // click was on a cell
        {
                for(int x = 0; x < size; x++)
                {
                    for( int y = 0; y < size; y++)
                    {
                        if(ae.getSource() == buttons[x][y])
                        {
                            switch (counts[x][y]) {
                                case MINE:
                                    buttons[x][y].setForeground(Color.RED);
                                    buttons[x][y].setIcon(new ImageIcon("")); // add bomb image
                                    takeTheL(1);                                    //user clicked on a mine
                                    break;
                                case 0:
                                    buttons[x][y].setText(counts[x][y] +"");
                                    buttons[x][y].setEnabled(false);
                                    ArrayList<Integer> clear = new ArrayList<>();    
                                    clear.add(x*100+y);
                                    dominoEffect(clear); // To recursively clear all surrounding '0' cells.
                                    takeTheW(); //checks win every move
                                    break;
                                default:
                                    buttons[x][y].setText(""+counts[x][y]);
                                    buttons[x][y].setEnabled(false);
                                    takeTheW();                                          // its a number > 0 and not a mine, so just check for win
                                    break;
                            }
                        }    
                    }
                }
        }


    }
    /**
     * Function creates mines at random positions.
     * @param s the size of the board(row or column count)
     */

    public void createMines(int s){
    ArrayList<Integer> list = new ArrayList<>();  //Modifiable array to store pos. of mines.
        for(int x = 0; x < s; x++)
        {
            for(int y = 0; y < s; y++)
            {
                list.add(x*100+y);                       // x & y shall be individually retrieved by dividing by 100 and modulo 100 respectively.
                                                         // refer to lines 284 and 285 for implementation
            }
        }
        counts = new int[s][s];                    //resetting back-end array

        for(int a = 0; a < (int)(s * 1.5); a++)
        {
            int choice = (int)(Math.random() * list.size());
            counts [list.get(choice) / 100] [list.get(choice) % 100] = MINE;      //Using corollary of before-last comment to set mines as well.
            list.remove(choice);                                                                           // We don't want two mines in the same pos., so remove that pos. from list.
        }
        /*
        Following segment initializes 'neighbor counts' for each cell. That is, the number of 
        mines that are present in the eight surrounding cells. IF the cell isn't a mine.
        Note : It is done in the back-end array as that contains the numbers (MINE or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8)
        */
        for(int x = 0; x < s; x++)
        {
           for(int y = 0; y < s; y++)
           {
            if(counts[x][y] != MINE)
            {
                int neighbor = 0;
                if( x > 0 && y > 0 && counts[x-1][y-1] == MINE) //top left
                {
                    neighbor++;
                }
                if( y > 0 && counts[x][y-1] == MINE) //left
                {
                    neighbor++;
                }
                if( y < size - 1 && counts[x][y+1] == MINE) //right
                {
                    neighbor++;
                }
                if( x < size - 1 && y > 0 && counts[x+1][y-1] == MINE) //bottom left
                {
                    neighbor++;
                }
                if( x > 0 && counts[x-1][y] == MINE) //up
                {
                    neighbor++;
                }
                if( x < size - 1 && counts[x+1][y] == MINE)//down
                {
                    neighbor++;
                }
                if( x > 0 && y < size - 1 &&counts[x-1][y+1] == MINE) //top right
                {
                    neighbor++;
                }
                if( x < size - 1 && y < size - 1 && counts[x+1][y+1] == MINE) //bottom right
                {
                    neighbor++;
                }
                counts[x][y] = neighbor;                        //setting value
            }
           }
        }
    }


    /**
     * This function, called the domino effect, is an implementation of the idea that,
     * when a cell with no surrounding mines is clicked, there's no point in user clicking
     * all eight surrounding cells. Therefore, all surrounding
     * cells' counts will be displayed in corresponding cells. 
     * The above is done recursively.
     * @param toClear the ArrayList which is passed to the function with positions in array
     *                that are zero, and are subsequently clicked.
     */

    public void dominoEffect(ArrayList<Integer> toClear){
        if(toClear.isEmpty())
            return;                         //base case

        int x = toClear.get(0) / 100;       //getting x pos.
        int y = toClear.get(0) % 100;       //getting y pos.
        toClear.remove(0);                  //remove that element from array to prevent infinite recursion.    
            if(counts[x][y] == 0)
            {                               //similar to neighbor counts, each surrounding cell is filled   

                if( x > 0 && y > 0 && buttons[x-1][y-1].isEnabled()) //top left
                {
                    buttons[x-1][y-1].setText(counts[x-1][y-1] + "");
                    buttons[x-1][y-1].setEnabled(false);
                    if(counts[x-1][y-1] == 0)
                    {
                        toClear.add((x-1)*100 + (y-1));     //to recursively implement, each surrounding cell is the new cell,
                                                                              // the surrounding cells of which we shall check and so on.
                    }
                }
                if( y > 0 && buttons[x][y-1].isEnabled()) //left
                {
                    buttons[x][y-1].setText(counts[x][y-1] + "");
                    buttons[x][y-1].setEnabled(false);
                    if(counts[x][y-1] == 0)
                    {
                        toClear.add(x*100 + (y-1));
                    }

                }
                if( y < size - 1 && buttons[x][y+1].isEnabled()) //right
                {
                    buttons[x][y+1].setText(counts[x][y+1] + "");
                    buttons[x][y+1].setEnabled(false);
                    if(counts[x][y+1] == 0)
                    {
                        toClear.add(x*100 + (y+1));
                    }

                }
                if( x < size - 1 && y > 0 && buttons[x+1][y-1].isEnabled()) //bottom left
                {
                    buttons[x+1][y-1].setText(counts[x+1][y-1] + "");
                    buttons[x+1][y-1].setEnabled(false);
                    if(counts[x+1][y-1] == 0)
                    {
                        toClear.add((x+1)*100 + (y-1));
                    }

                }
                if( x > 0 && buttons[x-1][y].isEnabled()) //up
                {
                    buttons[x-1][y].setText(counts[x-1][y] + "");
                    buttons[x-1][y].setEnabled(false);
                    if(counts[x-1][y] == 0)
                    {
                        toClear.add((x-1)*100 + y);
                    }

                }
                if( x < size - 1 && buttons[x+1][y].isEnabled())//down
                {
                    buttons[x+1][y].setText(counts[x+1][y] + "");
                    buttons[x+1][y].setEnabled(false);
                    if(counts[x+1][y] == 0)
                    {
                        toClear.add((x+1)*100 + y);
                    }

                }
                if( x > 0 && y < size - 1 && buttons[x-1][y+1].isEnabled()) //top right
                {
                    buttons[x-1][y+1].setText(counts[x-1][y+1] + "");
                    buttons[x-1][y+1].setEnabled(false);
                    if(counts[x-1][y+1] == 0)
                    {
                        toClear.add((x-1)*100 + (y+1));
                    }

                }
                if( x < size - 1 && y < size - 1 && buttons[x+1][y+1].isEnabled()) //bottom right
                {
                    buttons[x+1][y+1].setText(counts[x+1][y+1] + "");
                    buttons[x+1][y+1].setEnabled(false);
                    if(counts[x+1][y+1] == 0)
                    {
                        toClear.add((x+1)*100 + (y+1));
                    }

                }
            }
            dominoEffect(toClear);      //recursive call with list containing surrounding cells, for further check-and-clear of THEIR surr. cells.
    }

    //Main method.
    public static void main(String[] args){
        new Minesweeper(20);    // Can be made of any size. (For now only squares)


    }

    @Override
    public void mouseClicked(MouseEvent me) {
        if (SwingUtilities.isRightMouseButton(me)){
            // TODO : Handle flagging of mines.
        }
    }

    @Override
    public void mousePressed(MouseEvent me) {
     // Do nothing
    }

    @Override
    public void mouseReleased(MouseEvent me) {
     // Do nothing
    }

    @Override
    public void mouseEntered(MouseEvent me) {
        // Do nothing
    }

    @Override
    public void mouseExited(MouseEvent me) {
       // Do nothing
    }

}