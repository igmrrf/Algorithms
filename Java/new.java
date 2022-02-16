public void dfs(Vertex vertex){
  vertex.setVisited(true);
  print(vertex);

  for(Vertex v: vertex.neighbours()){
    if(!v.isVisited()){
      dfs(v);
    }
  }
}

public void dfs(Vertex vertex){
  Stack stack;
  stack.push(vertex);

  while(!stack.isEmpty()){
    actual = stack.pop();
    for(Vertex v: actual.neighbours()){
      if(v.isVisited()){
        v.setVisited(true);
        stack.push(v);
      }
    }
  }
}