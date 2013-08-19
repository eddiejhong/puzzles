<?php

class numberConversion{
	function numberToBinary($n = 2){
		while(!isset($binaryArray[0])){
			
			$largestPower = floor(log($n, 2));

			$largestProduct = pow(2,$largestPower);
			$binaryArray[$largestPower] = 1;
			$n -= $largestProduct;
			var_dump($n);
			if($n == 1){
				$binaryArray[0] = 1;
			}
			if($n == 0){
				break;
			}
		}

		return $binaryArray;
	}
}

$numberConversion = new numberConversion();
$x = 20;
$answer = $numberConversion->numberToBinary($x);
$answer = implode("",$answer);
echo "The number {$x} in binary for is {$answer}";

?>