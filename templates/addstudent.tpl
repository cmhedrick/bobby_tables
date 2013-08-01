<h1>Add Student</h1>

<p>Please Fillout student information</p>
<form method="post" action="/added">
  %for column in column_list:
    <label>{{column}} <input name="{{column}}" type="text" style="width:  500px;"></label>
  %end
  <button type="submit">Submit</button>
</form>

%rebase templates/base.tpl title='Add Student'
