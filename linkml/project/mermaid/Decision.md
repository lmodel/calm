


```mermaid
 classDiagram
    class Decision
    click Decision href "../Decision"
      Decision : controls
        
          
    
        
        
        Decision --> "0..1" Control : controls
        click Control href "../Control"
    

        
      Decision : Decision_description
        
      Decision : Decision_nodes
        
          
    
        
        
        Decision --> "1..*" Node : Decision_nodes
        click Node href "../Node"
    

        
      Decision : Decision_relationships
        
          
    
        
        
        Decision --> "1..*" Relationship : Decision_relationships
        click Relationship href "../Relationship"
    

        
      
```
