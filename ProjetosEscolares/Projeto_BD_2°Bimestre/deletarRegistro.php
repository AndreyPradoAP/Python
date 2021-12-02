<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
		<link rel="stylesheet" type="text/css" href="estiloPáginas.css" media="screen">
		<title>Inserção Dados</title>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
	</head>
	<body>
		<div class="jumbotron">
	  			<h1>Greenpeace</h1>     
	  			<p>Monitoramento do derretimento calotas polares</p>  
		</div>

		<?php
			include "conexaoBD.php";

			$dataHora = $_GET['dataHora'];

			$sql = "DELETE FROM vw_derretimentoGelo WHERE dataHora = '$dataHora'";
			mysqli_query($con, $sql) or die ("Erro ao deletar o registro");
			mysqli_close($con);

			echo "registro deletado com sucesso!<br><br>";
			echo "<a href='index.html'>Clique aqui para voltar à página inicial</a> <br>";
			echo "<a href='selecionarDados.php'>Clique aqui para ver todos os registros</a> <br>";
		?>
	</body>
</html>