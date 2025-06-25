<?php 
  $a = "Osama";
  $b = &$a;
  $b = "test";
  $a = "text";

  echo $a;
  echo '<br>';
  echo $b;