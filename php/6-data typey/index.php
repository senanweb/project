<?php
    /*
        bool > Boolean =tru or false
        int=> Integer
        float => Floating Point Number |- double
        string
        array
        Other Types
        gettype()
    */
    echo gettype(true);
    echo '<br>';
    echo gettype(10);
    echo '<br>';
    echo gettype('true');
    echo '<br>';
    echo gettype(1.5);
    echo '<br>';
    echo gettype(array("EG" => "Egypt", "KSA" => "Saudi Arb"));
    echo '<br>';
    echo gettype([5,'test']);
    echo '<br>';
