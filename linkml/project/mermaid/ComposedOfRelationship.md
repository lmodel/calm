


```mermaid
 classDiagram
    class ComposedOfRelationship
    click ComposedOfRelationship href "../ComposedOfRelationship"
      ComposedOfRelationship : ComposedOfRelationship_nodes
        
          
    
        
        
        ComposedOfRelationship --> "1..*" Node : ComposedOfRelationship_nodes
        click Node href "../Node"
    

        
      ComposedOfRelationship : container
        
      
```
