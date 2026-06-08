


```mermaid
 classDiagram
    class DeployedInRelationship
    click DeployedInRelationship href "../DeployedInRelationship"
      DeployedInRelationship : container
        
      DeployedInRelationship : DeployedInRelationship_nodes
        
          
    
        
        
        DeployedInRelationship --> "1..*" Node : DeployedInRelationship_nodes
        click Node href "../Node"
    

        
      
```
