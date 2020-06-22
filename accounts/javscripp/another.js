import { Person } from "./person";

export class AnotherPerson extends Person {
    constructor(name,degree){
        super(name);
        this.degree=degree;
    }
   teach(){
       console.log("Someone is teaching ");
   }
}
