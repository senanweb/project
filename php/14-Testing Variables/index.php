<?php
    $name = "sinan";
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Php Page | <?php echo $name; ?></title>
</head>
<body>
    <div>
        <h1>Welcome To <?php echo $name; ?></h1>
    </div>
    <div>
        <p>Just test</p>
    </div>
    <div>
        <?php include("print.php") ?>
    </div>
</body>
</html>