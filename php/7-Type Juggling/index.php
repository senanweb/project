<?php
/*
 Data Types
 Type Juggling + Automatic Type Conversion
*/
    echo 1 + '2';
    echo '<br>';
    echo True; // 1
    echo '<br>';
    echo gettype(True); // Boolean
    echo '<br>';
    echo True + True; // 2
    echo '<br>';
    echo gettype(True + True); // Integer
    echo '<br>';