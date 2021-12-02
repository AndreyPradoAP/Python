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
			include "conexaoBD.php";

			$sql = "SELECT * FROM vw_derretimentoGelo";
			$res = mysqli_query($con, $sql) or die ("Erro ao selecionar o registros, tente novamente");

			while ($i = mysqli_fetch_array($res)) {
				echo "Pesquisador responsável: ".$i['nomePesquisadorResponsavel']."<br>";
				echo "Data e hora do cadastro da pesquisa: ".$i['dataHora']."<br>";
				echo "Derretimento semestral das calotas: ".$i['derretimentoSemestral']." toneladas<br>";
				echo "Elevação do nível do mar: ".$i['elevacaoMar']." milimetros<br>";	
				echo"<br><br>";
			}
			echo "<a href='index.html'>Clique aqui para voltar à página inicial</a><br>";
		?>		
	</body>
</html>