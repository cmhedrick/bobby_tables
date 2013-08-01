<h1>Hilt Institute Student Database</h1>
<table>
  <tr>
    <th>Student ID</th>
    <th>First Name</th>
    <th>Last Name</th>
    <th>Date of Birth</th>
  </tr>
  %for row in data:
  <tr>
    %for col in row:
    <td>{{col}}</td>
    %end
  </tr>
  %end
</table>
<a href="/addstudent">Add Student</a>

%rebase templates/base.tpl title='Home'
