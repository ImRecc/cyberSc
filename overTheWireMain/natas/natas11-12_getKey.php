<?php
// kBSwkBSwkBSwkBSwkBSwkBSwkBZ{GvF"R)
//repeating, length=4
$cookie = "EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0%2FGBlgaVVIJDURDSQ1VRY%3D";

// 2. Decode it back to Binary Gibberish
$encrypted = base64_decode($cookie);

// 3. The default plaintext
$plainText = json_encode(array("showpassword"=>"no", "bgcolor"=>"#ffffff"));

// 4. XOR them together to find the key!
$key = "";
for($i=0; $i<strlen($plainText); $i++) {
    $key .= $plainText[$i] ^ $encrypted[$i];
}

print("The repeating key is: " . $key . "\n");
?>
