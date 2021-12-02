<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
		<link rel="stylesheet" type="text/css" href="estiloPáginas.css" media="screen">
		<title></title>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
	</head>
	<body>
		<div class="jumbotron">
	  			<h1>Greenpeace</h1>     
	  			<p>Monitoramento do derretimento calotas polares</p>  
		</div>

		<?php
			$anoAtual = $_GET['anoAtual'];
			$anoPrevisao = $_GET['anoPrevisao'];

			$nivelMarAno = ($anoPrevisao - $anoAtual) * 0.665;
			$derretimentoGeloAno = ($anoPrevisao - $anoAtual) * 256000000;

			echo "No ano de $anoPrevisao, o nivel do mar subirá $nivelMarAno cm e haverá $derretimentoGeloAno toneladas de gelo derretido<br>";
			echo "<a href='index.html'>Clique aqui para voltar à página inicial</a><br>";
			echo "<a href='selecionarDados.php'>Clique aqui para ver todos os registros</a><br>";
		?>
	</body>
</html>

