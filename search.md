---
layout: page
title: Search
header: Search
scripts: [search.js]
---
{% include JB/setup %}

<h2>Search results</h2>
<ul class="posts">
    <span class='no-matches' style="display:none">No results found</span>
  {% for post in site.posts %}
    <li style="display:none"><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a>
    {% if post.category == "Example"%}<span class="label label-warning">Example</span>{% endif %}
    {% if post.category == "Tutorial"%}<span class="label label-success">Tutorial</span>{% endif %}
    </li>
  {% endfor %}
  {% for doc in site.docs %}
    <li style="display:none"><span>{{ doc.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ doc.url }}">{{ doc.title }}</a> <span class="label label-primary">Docs</span></li>
  {% endfor %}
</ul>
<script>
var search_data = [
  {% for post in site.posts %}
    {
      "title"    : "{{ post.title | escape }}",
      "category" : "{{ post.category }}",
      "tags"     : "{{ post.tags | join: ', ' }}",
      "url"      : "{{ site.baseurl }}{{ post.url }}",
      "date"     : "{{ post.date }}",
      "content"  : "{{ post.content | strip_html | strip_newlines | escape }}"
    } {% unless forloop.last %},{% endunless %}
  {% endfor %}
];

var docs_data = [
  {% for doc in site.docs %}
    {
      "title"    : "{{ doc.title | escape }}",
      "category" : "",
      "tags"     : "",
      "url"      : "{{ site.baseurl }}{{ doc.url }}",
      "date"     : "{{ doc.date }}",
      "content"  : "{{ doc.content | strip_html | strip_newlines | escape }}"
    } {% unless forloop.last %},{% endunless %}
  {% endfor %}
];

search_data = search_data.concat(docs_data)

</script>
