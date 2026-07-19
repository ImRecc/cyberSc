<?php
$real_key = "kBSw"; // Put the 4-letter key you found here!

$desiredPlainText = json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff"));

// The developer's exact encryption function
$outText = "";
for($i=0; $i<strlen($desiredPlainText); $i++) {
    $outText .= $desiredPlainText[$i] ^ $real_key[$i % strlen($real_key)];
}

// Base64 encode it so it's safe for the browser
print("Your new cookie is: " . base64_encode($outText) . "\n");
?>
