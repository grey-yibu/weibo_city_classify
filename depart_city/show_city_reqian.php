
<?php
    require('/data1/sinawap/code/place/lbsapi/internalapi/common.php');
    require_once '/data1/sinawap/code/place/lbsapi/internalapi/lib/Common/SingletonRedis.php';
    require_once '/data1/sinawap/code/place/lbsapi/internalapi/function/private_letter_city_data.php';




    $filename = "all_city_sort";
    $handle = fopen($filename, "r");
    $contents = fread($handle, filesize ($filename));
    fclose($handle);

    $tmp_json_array  =  json_decode( $contents);

    $new_city  =  array();

    foreach ($tmp_json_array as $city_id) {
        $tmp_city_name  =  "";
        if ( isset($PRIVATE_GUONEI_CITY[ $city_id ]) ){
            $tmp_city_name  =  $PRIVATE_GUONEI_CITY[ $city_id ];
        }if ( isset($PRIVATE_GUONEI_PROVINCE[ $city_id ]) ){
            $tmp_city_name  =  $PRIVATE_GUONEI_PROVINCE[ $city_id ];
        }if ( isset($PRIVATE_GUOWAI_CITY[ $city_id ]) ){
            $tmp_city_name  =  $PRIVATE_GUOWAI_CITY[ $city_id ];
        }

        $new_city[] = $tmp_city_name;
        
    }

    $new_city_str = json_encode($new_city,  JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    echo  $new_city_str;


?>
