<!-- 
  MySQL Table:
    CREATE TABLE studentrecord_tbl ( 
      studid TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
      lastname VARCHAR(30) NOT NULL,
      firstname VARCHAR(30) NOT NULL,
      prelim DECIMAL(4,2) UNSIGNED NOT NULL,
      midterm DECIMAL(4,2) UNSIGNED NOT NULL,
      finals DECIMAL(4,2) UNSIGNED NOT NULL,
      final_grade DECIMAL(4,2) UNSIGNED NOT NULL,
      PRIMARY KEY (studid)
    );
-->



<?php
  //Connection Parameters
  $servername = "localhost";
  $username = "root"; 
  $password = ""; 
  $dbname = "studentrecord_db"; 
  $conn = new mysqli($servername, $username, $password, $dbname);
  if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
  } 

  //Insert process
  if (isset($_POST['Submit'])) {
    //Set Variables
    $var_lname = $_POST['lnameInput'];
    $var_fname = $_POST['fnameInput'];
    $var_prelim = $_POST['prelimInput'];
    $var_midterm = $_POST['midtermInput'];
    $var_finals = $_POST['finalsInput'];
    $var_fgrade = (($var_prelim+$var_midterm+$var_finals) / 3);
    
    //SQL Query to Insert
    $sql = "INSERT INTO studentrecord_tbl VALUES (DEFAULT, '$var_lname', '$var_fname', '$var_prelim', '$var_midterm', '$var_finals', $var_fgrade)";
    
    //Checks if page is in a function mode, 0 for Delete, 1 for Update
    if ($_GET['function'] == '1'){
      $upd_id = $_GET['id'];
      //SQL Query to Update
      $sql = "UPDATE studentrecord_tbl SET lastname = '$var_lname', firstname = '$var_fname',prelim = '$var_prelim',midterm = '$var_midterm',finals = '$var_finals' ,final_grade = '$var_fgrade' WHERE studid = '$upd_id'"; 
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


    //Delete Function
    if (isset($_GET['id']) && $_GET['function'] == '0') {
        $del_id = $_GET['id'];
        $del_sql = "DELETE FROM studentrecord_tbl WHERE studid='$del_id'";
        $del_result = $conn->query($del_sql);
        if ($del_result == TRUE) {
            header('Location: localhost');
        }else{
            echo "Error:" . $sql . "<br>" . $conn->error;
        }
    } 

      //SQL Query to display table content
  $disp_sql = "SELECT * FROM studentrecord_tbl";

  if ($_GET['disp_mode'] == '1') {
    $disp_sql = "SELECT * FROM studentrecord_tbl WHERE finals='82.6'";
  }else if($_GET['disp_mode'] == '2'){
    $disp_sql = "SELECT * FROM studentrecord_tbl WHERE prelim='75'";
  }else if($_GET['disp_mode'] == '3'){
    $disp_sql = "SELECT * FROM studentrecord_tbl ORDER BY final_grade,firstname";
  }else if($_GET['disp_mode'] == '4'){
    $disp_sql = "SELECT * FROM studentrecord_tbl WHERE final_grade>='87'";
  }

  $disp_result = $conn->query($disp_sql);

?>

<!DOCTYPE html>
<html>
    <head>
        <title>CRUD Activity PHP</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
    </head>
    <body>
        
            <h2><center>Student Records Database</h2></center>

    <?php
    $Button_Val="Insert";

    if ($_GET['function'] == '1') {
      $Button_Val="Update";
      $stud_id = $_GET['id']; 
      $disp_upd_sql = "SELECT * FROM studentrecord_tbl WHERE studid='$stud_id'";
      $disp_upd_result = $conn->query($disp_upd_sql); 
      if ($disp_upd_result->num_rows > 0) {        
        while ($row = $disp_upd_result->fetch_assoc()) {
            $INPUT_LNAME = $row['lastname'];
            $INPUT_FNAME = $row['firstname'];
            $INPUT_PRELIM = $row['prelim'];
            $INPUT_MIDTERM = $row['midterm'];
            $INPUT_FINALS = $row['finals'];
        }
      }
    } 
    ?>

    <div class="container">
    <form action="" method="POST">
    <fieldset>
    <table class="table">
        <thead>
            <tr>
            <th>LASTNAME</th>
            <th>FIRSTNAME</th>
            <th>PRELIM</th>
            <th>MIDTERM</th>
            <th>FINALS</th>
        </tr>
        </thead>
        <tbody> 
            <tr>
            <td><input type="text" maxlength="30" name="lnameInput" value="<?php echo $INPUT_LNAME; ?>" required></td>
            <td><input type="text" maxlength="30" name="fnameInput" value="<?php echo $INPUT_FNAME; ?>" required></td>
            <td><input type="number" maxlength="4" name="prelimInput" step=".01" max="99" value="<?php echo $INPUT_PRELIM; ?>" required></td>
            <td><input type="number" maxlength="4" name="midtermInput" step=".01" max="99" value="<?php echo $INPUT_MIDTERM; ?>" required></td>
            <td><input type="number" maxlength="4" name="finalsInput" step=".01" max="99" value="<?php echo $INPUT_FINALS; ?>" required></td>
            </tr>
        </tbody>
      </table>
      <input type="submit" name="Submit" value="<?php echo $Button_Val; ?>">
    </fieldset>
    </form> 
    </div>

    <h2><center>Display Buttons</h2></center>
    <div class="container">
    <fieldset>
    <table class="table">
        <thead>
            <tr>
            <th>Show all</th>
            <th>Show students with finals grade of 82.6</th>
            <th>Show students with prelim grade of 75</th>
            <th>Sort by final grade then first name</th>
            <th>Show students with final grade greater or equal to 87</th>
        </tr>
        </thead>
        <tbody> 
            <tr>
            <td><a class="btn btn-info" href="CRUDact1.php">Display</a>&nbsp;</td>
            <td><a class="btn btn-info" href="CRUDact1.php?disp_mode=1">Display</a>&nbsp;</td>
            <td><a class="btn btn-info" href="CRUDact1.php?disp_mode=2">Display</a>&nbsp;</td>
            <td><a class="btn btn-info" href="CRUDact1.php?disp_mode=3">Display</a>&nbsp;</td>
            <td><a class="btn btn-info" href="CRUDact1.php?disp_mode=4">Display</a>&nbsp;</td>
            </tr>
        </tbody>
      </table>
      </fieldset>
    </div><br><br><br>








    <div class="container">
    <table class="table">
        <thead>
            <tr>
            <th>studid</th>
            <th>lastname</th>
            <th>firstname</th>
            <th>prelim</th>
            <th>midterm</th>
            <th>finals</th>
            <th>final_grade</th>
        </tr>
        </thead>
        <tbody> 
            <?php
                if ($disp_result->num_rows > 0) {
                    while ($row = $disp_result->fetch_assoc()) {
            ?>
                        <tr>
                        <td><?php echo $row['studid']; ?></td>
                        <td><?php echo $row['lastname']; ?></td>
                        <td><?php echo $row['firstname']; ?></td>
                        <td><?php echo $row['prelim']; ?></td>
                        <td><?php echo $row['midterm']; ?></td>
                        <td><?php echo $row['finals']; ?></td>
                        <td><?php echo $row['final_grade']; ?></td>
                        <td>
                            <a class="btn btn-info" href="CRUDact1.php?id=<?php echo $row['studid']; ?>&function=1">Edit</a>&nbsp;
                            <a class="btn btn-danger" href="CRUDact1.php?id=<?php echo $row['studid']; ?>&function=0">Delete</a></td>
                        </tr>                       

            <?php       
                    }
                }
            ?>                
        </tbody>
    </table>
        </div>



    
    </body>
</html>

