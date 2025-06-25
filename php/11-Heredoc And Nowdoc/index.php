<?php
    $name = "Osama";
    echo <<<"Here"
    Hello PHP
    Special Characters $$$  \\\\
    Hello My Name Is $name
    Here;
    echo '<br>';
    // ========
    echo <<<'Now'
    Hello PHP
    Special Characters $$$  \\\\
    Hello My Name Is $name
    Now;
    // ========
    echo '<br>';
    // ========
    echo '<ul>';
        echo "<li>" . $name . "</li>";
        echo "<li>" . $name . "</li>";
        echo "<li>" . $name . "</li>";
        echo "<li>" . $name . "</li>";
    echo '</ul>';

    echo <<<"navlinks"
      <ul>
        <li>$name</li>
        <li>$name</li>
        <li>$name</li>
      </ul>
    navlinks;