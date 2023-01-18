<?php
class Steven
{
    private $name;
    private $age;
    private $gender;

    public function __construct($name, $age, $gender)
    {
        $this->name = $name;
        $this->age = $age;
        $this->gender = $gender;
    }

    public function getName()
    {
        return $this->name;
    }

    public function setName($name)
    {
        $this->name = $name;
    }

    public function getAge()
    {
        return $this->age;
    }

    public function setAge($age)
    {
        $this->age = $age;
    }

    public function getGender()
    {
        return $this->gender;
    }

    public function setGender($gender)
    {
        $this->gender = $gender;
    }

    public function __toString()
    {
        return "Name: " . $this->name . ", Age: " . $this->age . ", Gender: " . $this->gender;
    }

    public function saveToDB()
    {
        $conn = new PDO("mysql:host=localhost;dbname=mydb", "root", "password");
        $stmt = $conn->prepare("INSERT INTO person (name, age, gender) VALUES (:name, :age, :gender)");
        $stmt->bindParam(':name', $this->name);
        $stmt->bindParam(':age', $this->age);
        $stmt->bindParam(':gender', $this->gender);
        $stmt->execute();
    }
}

$steven = new Steven("Steven", 30, "Male");
echo $steven;
$steven->saveToDB();
?>

