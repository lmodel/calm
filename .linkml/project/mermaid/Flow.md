


```mermaid
 classDiagram
    class Flow
    click Flow href "../Flow"
      Flow : controls
        
          
    
        
        
        Flow --> "0..1" Control : controls
        click Control href "../Control"
    

        
      Flow : Flow_description
        
      Flow : metadata
        
      Flow : name
        
      Flow : requirement_url
        
      Flow : transitions
        
          
    
        
        
        Flow --> "1..*" Transition : transitions
        click Transition href "../Transition"
    

        
      Flow : unique_id
        
      
```
