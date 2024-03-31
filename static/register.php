<?php
// Step 2: Establish MySQL database connection
$servername = "localhost";
$username = "root";
$password = "VivMus@2024";
$database = "evolveguru";

$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
else {
    $stmt = $conn ->prepare("insert into registration(name, email, password, mob_no, profession)
    values(?, ?, ?, ?, ?)");
    $stmt ->bind_param("sssss", $name, $email, $password, $mob_no, $profession);
    $stmt->execute();
    echo "Registration successfull!";
    $stmt->close();
    $conn->close();

}

?>
