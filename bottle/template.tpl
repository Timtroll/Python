<!DOCTYPE html>
<html>
  <head>
    <title>Messages</title>
  </head>
  <body>
    <table>
      <tr>
        <th>id</th>
        <th>message</th>
      </tr>
      % for m in messages:
      <tr>
        <td>{{ m.id }}</td>
        <td>{{ m.content }}</td>
      </tr>
      % end
  </body>
</html>