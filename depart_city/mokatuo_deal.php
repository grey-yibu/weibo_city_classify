<?php
require_once('/data1/sinawap/code/place/lbsapi/internalapi/function/mercator.php');
require_once('/data1/sinawap/code/place/lbsapi/internalapi/function/quadkeyEx.php');


$file_path = $argv[1] ;
if(file_exists($file_path)){
    $fp = fopen($file_path,"r");
    while(!feof($fp)){
        $str = fgets($fp);//逐行读取。如果fgets不写length参数，默认是读取1k。
        
        $tmp_zu = explode("{@}", $str);
        $time_tmp = date("Y-m", strtotime($tmp_zu[0]));
        $uid_tmp   = $tmp_zu[1];
        $city_str  = $tmp_zu[11];
        $tmp_content = $tmp_zu[7];

        $city_zu  =  explode(" ", $city_str);
        $city_id  =  $city_zu[3];
        $city_id  =  substr($city_id, 0, 9)."0000000000";
        if(substr($city_id, 0, 5)!="80086"){
            continue;
        }

        $tmp_content = str_replace(array("\r\n", "\r", "\n"), ' ', $tmp_content);
        $pattern      =  '/(http):\/\/([^\s]+)/i';
        $tmp_content  =  preg_replace($pattern,'',$tmp_content);
        $bad_filter = '/下载|聊聊天就是最好的陪伴|直播|阴阳师|绿洲|客户端/';
        if(preg_match($bad_filter,$tmp_content)) 
           continue; 

        if (  strlen($city_id)!=19 )
            continue;

        $tmp_fn=__DIR__."/log/{$city_id}";
        $tmp_fp=fopen($tmp_fn,"a+");
        fwrite($tmp_fp, $tmp_content."\n");
        fclose($tmp_fp);
    }
    fclose($fp);
}

?>


