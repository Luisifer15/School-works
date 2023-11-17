<!-- 
  MySQL Table:
    CREATE TABLE Cars ( 
      ID TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
      MAKE VARCHAR(20) NOT NULL,
      MODEL VARCHAR(50) NOT NULL,
      YEAR SMALLINT(4) UNSIGNED NOT NULL,
      COLOR VARCHAR(35) NOT NULL,
      STOCK BOOLEAN NOT NULL,
      DATE_RECORDED TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      DATE_MODIFIED TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY (ID)
    );
-->



<?php
  //Connection Parameters
  $servername = "localhost";
  $username = "root"; 
  $password = ""; 
  $dbname = "CRUD"; 
  $conn = new mysqli($servername, $username, $password, $dbname);
  if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
  } 

  //SQL Qery to display table content
  $disp_sql = "SELECT * FROM Cars";
  $result = $conn->query($disp_sql);

  //SUBMIT.POST_
  if (isset($_POST['Submit'])) {
    
    /*ID
    MAKE
    MODEL
    YEAR
    COLOR
    STOCK
    DATE_RECORDED
    DATE_MODIFIED*/

    //Set Variables
    $var_Make = $_POST['MakeInput'];
    $var_Model = $_POST['ModelInput'];
    $var_Year = $_POST['YearInput'];
    $var_Color = $_POST['ColorInput'];
    if(isset($_POST['StockInput'])) $var_Stock = 1; else $var_Stock = 0;
    
    //SQL Query to Insert
    $sql = "INSERT INTO Cars VALUES (DEFAULT, '$var_Make', '$var_Model', '$var_Year', '$var_Color', '$var_Stock', DEFAULT, DEFAULT)";
    
    //Checks if page is in a function mode, 0 for Delete, 1 for Update
    if ($_GET['function'] == '1'){
      $upd_id = $_GET['id'];
      //SQL Query to Update
      $sql = "UPDATE Cars SET MAKE = '$var_Make', MODEL = '$var_Model',YEAR = '$var_Year',COLOR = '$var_Color',STOCK = '$var_Stock' WHERE ID = '$upd_id'"; 
    }

    //Sends Query
    $result = $conn->query($sql);
    
    //SQL query status
    if ($result == TRUE) {
      header('Location: localhost');
      echo "Success";
    }else{
      echo "Error: ". $sql . "<br>". $conn->error;
    } 
  } 

    if (isset($_GET['id']) && $_GET['function'] == '0') {
        $del_id = $_GET['id'];
        $del_sql = "DELETE FROM Cars WHERE ID='$del_id'";
         $result = $conn->query($del_sql);
         if ($result == TRUE) {
            echo "Record deleted successfully.";
            $sql = "SELECT * FROM Cars";
            $result = $conn->query($sql);
        }else{
            echo "Error:" . $sql . "<br>" . $conn->error;
        }
    } 
?>

<!DOCTYPE html>
<html>
    <head>
        <title>CRUD PHP</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h2>Garage Database</h2>
    <table class="table">
        <thead>
            <tr>
            <th>ID</th>
            <th>MAKE</th>
            <th>MODEL</th>
            <th>YEAR</th>
            <th>COLOR</th>
            <th>STOCK</th>
            <th>DATE_RECORDED</th>
            <th>DATE_MODIFIED</th>
        </tr>
        </thead>
        <tbody> 
            <?php
                if ($result->num_rows > 0) {
                    while ($row = $result->fetch_assoc()) {
            ?>
                        <tr>
                        <td><?php echo $row['ID']; ?></td>
                        <td><?php echo $row['MAKE']; ?></td>
                        <td><?php echo $row['MODEL']; ?></td>
                        <td><?php echo $row['YEAR']; ?></td>
                        <td><?php echo $row['COLOR']; ?></td>
                        <td><?php if ($row['STOCK'] == 1) echo "Yes"; else echo "No"; ?></td>
                        <td><?php echo $row['DATE_RECORDED']; ?></td>
                        <td><?php echo $row['DATE_MODIFIED']; ?></td>
                        <td><a class="btn btn-info" href="CRUD.php?id=<?php echo $row['ID']; ?>&function=1">Edit</a>&nbsp;<a class="btn btn-danger" href="CRUD.php?id=<?php echo $row['ID']; ?>&function=0">Delete</a></td>
                        </tr>                       

            <?php       
                    }
                }
            ?>                
        </tbody>
    </table>
        </div>



    <?php
    $Button_Val="Insert";
    $INPUT_YEAR = '2023';
    $INPUT_STOCK = 1;

    if ($_GET['function'] == '1') {
      $Button_Val="Update";
      $car_id = $_GET['id']; 
      $disp_upd_sql = "SELECT * FROM Cars WHERE ID='$car_id'";
      $result = $conn->query($disp_upd_sql); 
      if ($result->num_rows > 0) {        
        while ($row = $result->fetch_assoc()) {
            $INPUT_MAKE = $row['MAKE'];
            $INPUT_MODEL = $row['MODEL'];
            $INPUT_YEAR = $row['YEAR'];
            $INPUT_COLOR = $row['COLOR'];
            $INPUT_STOCK = $row['STOCK'];
        }
      }
    } 
    ?>

    <div class="container">
    <form action="" method="POST">
    <fieldset>
     <h3><?php echo $Button_Val; ?> Values:</h3>
      Make:<br>
      <input type="text" maxlength="20" name="MakeInput" value="<?php echo $INPUT_MAKE; ?>" required><br><br>
      Model:<br>
      <input type="text" maxlength="50" name="ModelInput" value="<?php echo $INPUT_MODEL; ?>" required><br><br>
      Year:<br>
      <input type="number" min="1900" max="2023" step="1" value="<?php echo $INPUT_YEAR; ?>"  name="YearInput"/ required><br><br>
      Color:<br>
      <input type="text" maxlength="35" name="ColorInput" value="<?php echo $INPUT_COLOR; ?>" ><br><br>
      Stock:<br>
      <input type="checkbox" name="StockInput" <?php echo ($INPUT_STOCK == 1) ? "checked" : ""; ?>><br><br>
      <br>

      <input type="submit" name="Submit" value="<?php echo $Button_Val; ?>">
    </fieldset>
    </form> 
    </div>
    </body>
</html>

