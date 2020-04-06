<?php
        require_once '/data1/sinawap/code/place/lbsapi/internalapi/common.php';



$anti_spam_url = "http://safe.i.t.sina.com.cn/v4/common.php?s=3&t=31&a={\"size\":\"20000\"}";
$anti_spam_json = tauth_curl($auth_uid, $anti_spam_url);
var_dump(  $anti_spam_json  );

?>