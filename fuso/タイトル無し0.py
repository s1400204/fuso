<form action="{% url 'yamagumo.views.some_view' %}" method="post">
  {% csrf_token %}
  <input type="text" name="yamagumo" value="">
  ...
  <input type="submit" name="button_1" value="ボタン1"> 
  <input type="submit" name="button_2" value="ボタン2"> 
</form>