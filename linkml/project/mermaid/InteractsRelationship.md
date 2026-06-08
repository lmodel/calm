


```mermaid
 classDiagram
    class InteractsRelationship
    click InteractsRelationship href "../InteractsRelationship"
      InteractsRelationship : actor
        
      InteractsRelationship : InteractsRelationship_nodes
        
          
    
        
        
        InteractsRelationship --> "1..*" Node : InteractsRelationship_nodes
        click Node href "../Node"
    

        
      
```
