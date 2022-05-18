% include('header.tpl', title = "TODO app")
<p>Añadir una nueva tarea:</p>
<form action="/new" method="POST">
<input type="text" size="65" maxlength="100" name="task">
<input type="submit" name="save" value="Guardar">
</form>
<p>Las tareas actuales son las siguientes:</p>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Tarea</th>
            <th>Estado</th>
            <th colspan="2">Acciones</th>
        </tr>
        %for row in rows:
            <tr>
            %for i in range(3):
                %if i != 2:
                <td>{{row[i]}}</td>
                %else:
                    %if row[i] == 0:
                    <td>Cerrada</td>
                    %else:
                    <td>Abierta</td>
                    %end
                %end
            %end
                <td>
                    <form action="/edit/{{row[0]}}" method="GET">
                    <input type="submit" name="save" value="Editar">
                    </form>  
                </td>
                <td>
                    <form action="/delete/{{row[0]}}" method="GET">
                    <input type="submit" name="delete" value="Borrar">
                    </form>   
                </td>
            </tr>
        %end
    </table>