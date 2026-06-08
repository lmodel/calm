


```mermaid
 classDiagram
    class ConnectsRelationship
    click ConnectsRelationship href "../ConnectsRelationship"
      ConnectsRelationship : destination
        
          
    
        
        
        ConnectsRelationship --> "1" NodeInterface : destination
        click NodeInterface href "../NodeInterface"
    

        
      ConnectsRelationship : source
        
          
    
        
        
        ConnectsRelationship --> "1" NodeInterface : source
        click NodeInterface href "../NodeInterface"
    

        
      
```
