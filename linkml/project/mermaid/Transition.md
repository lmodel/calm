


```mermaid
 classDiagram
    class Transition
    click Transition href "../Transition"
      Transition : direction
        
          
    
        
        
        Transition --> "0..1" TransitionDirection : direction
        click TransitionDirection href "../TransitionDirection"
    

        
      Transition : relationship_unique_id
        
      Transition : sequence_number
        
      Transition : Transition_description
        
      
```
