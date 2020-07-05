<?php
$user = $_SERVER['HTTP_USER_AGENT'];
$file = '.txt';
$fp = fopen($file, "w") or die("Couldn't open $file for writing!");
fwrite($fp, $user) or die("Couldn't write values to file!"); 
fclose($fp);
?>
<style type="text/css">
img.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>

<img src=".jpg" alt="Binni" class="center" />
