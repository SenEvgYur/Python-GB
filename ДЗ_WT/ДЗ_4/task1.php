<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    $skills = [
        'Excel' => 70,
        '1C' => 65,
        'Word' => 55,
        'Adobe Photoshop' => 50,
    ];
    ?>
    <?php foreach ($skills as $skillName => $skillValue): ?>
        <p></p>
    <?php endforeach; ?>
    echo $skills
</body>

</html>