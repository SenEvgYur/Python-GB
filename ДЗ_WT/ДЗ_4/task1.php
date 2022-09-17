<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Скилы для резюме</title>
</head>

<body>
    <?php
    $skills = array('Excel' => 70,
        "1С" => 65, 'Word' => 55,
        'Adobe Photoshop' => 20,
    );
    foreach( $skills as $key => $value ){
        echo $key."\t=>\t".$value."\n";
    }
    ?>     
</body>

</html>