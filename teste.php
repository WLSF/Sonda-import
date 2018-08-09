<?php

if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$me = $MadelineProto->get_self();

\danog\MadelineProto\Logger::log($me);

if (!$me['bot']) {
    /*
    $MadelineProto->messages->sendMessage(['peer' => '@luiznn', 'message' => "Olá!\nObrigado por criar o MadelineProto !! <3"]);
    //$MadelineProto->channels->joinChannel(['channel' => '@MadelineProto']);

    try {
        $MadelineProto->messages->importChatInvite(['hash' => 'https://t.me/joinchat/Bgrajz6K-aJKu0IpGsLpBg']);
        $MadelineProto->messages->sendMessage(['peer' => 'https://t.me/joinchat/Bgrajz6K-aJKu0IpGsLpBg', 'message' => 'Testing MadelineProto!']);
    }
    catch (\danog\MadelineProto\RPCErrorException $e) {}
    */

    $uploadfile = $MadelineProto->messages->sendMedia([
      'peer' => '@luiznn',
      'media' => [
          '_' => 'inputMediaUploadedDocument',
          'file' => 'olamundo.txt',
          'attributes' => [
              ['_' => 'documentAttributeFilename', 'file_name' => 'olamundo2.txt']
          ]
      ]
  ]);

  $fileid =  $uploadfile["updates"]["1"]["message"]['media']['document']['id'];
  $acess_hash =  $uploadfile["updates"]["1"]["message"]['media']['document']['access_hash'];
  $date =  $uploadfile["updates"]["1"]["message"]['date'];
  $size =  $uploadfile["updates"]["1"]["message"]['media']['document']['size'];
  $filename =  $uploadfile["updates"]["1"]["message"]['media']['document']['attributes']['0']['file_name'];
  $date2 = date('d-m-Y', $date);
  $time = date('h:i:s', $date);

echo "\n" . '-------------------- INFO FILE! --------------------'.PHP_EOL;
 \danog\MadelineProto\Logger::log('Fileid: ' . $fileid);
 \danog\MadelineProto\Logger::log('Acess Hash: ' . $acess_hash);
 \danog\Madelineproto\Logger::log('Unix Date: '. $date);
 \danog\Madelineproto\Logger::log('Date: '. $date2);
  \danog\Madelineproto\Logger::log('Time: '. $time);
 \danog\MadelineProto\Logger::log('Size: '. $size);
 \danog\MadelineProto\Logger::log('Name: '. $filename);

/*
      $MadelineProto->messages->sendMedia([
      'peer' => '@luiznn', // chatid
      'media' => [
          '_' => 'inputMediaUploadedDocument',
          'file' => 'video.mp4', //file
          'attributes' => [
              ['_' => 'documentAttributeFilename', 'file_name' => 'video.mp4']
          ]
      ],
      'message' => '[This is the caption](https://t.me/MadelineProto)',
      'parse_mode' => 'Markdown'
  ]);
  $sentMessage = $MadelineProto->messages->sendMedia([
      'peer' => '@luiznn',
      'media' => [
          '_' => 'inputMediaDocumentExternal',
          'url' => 'http://dl3.softgozar.com/Files/Software/KMPlayer_4.2.1.4_Portable_Softgozar.com.exe',
      ],
      'message' => '[THE](https://telegram.me/PWR)',
      'parse_mode' => 'Markdown'
  ]);
*/
}
echo '-------------------- FIM! --------------------------'.PHP_EOL;
