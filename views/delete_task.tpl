% include('header.tpl', title = "Borrar tarea")
<p>Borrar tarea con ID = {{no}}</p>
<form action="/delete/{{no}}" method="POST">
  <p>Hac click para confirmar que deseas eliminar la tarea: </p>
  <p><b>{{old[0]}}</b></p>

  <input type="submit" name="delete" value="Borrar">
  <input type="submit" name="cancel" value="Cancelar">
</form>
% include('footer.tpl')