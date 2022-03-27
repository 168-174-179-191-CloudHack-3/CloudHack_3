# CloudHack_3

 | SRN | NAME | SECTION |
 | --- | --- | --- |
 | PES1UG19CS168 | Geetanjali Koya | C |
 | PES1UG19CS174 | Guruprasad N Bamane | C |
 | PES1UG19CS179 | Harivardhan | C |
 | PES1UG19CS191 | Ishwar Joshi | C |

Activity : creating/deploying application components that are independent of each other,which makes each service easily deployable,testable and maintainable.

Earlier the four functions **Addition,Subtraction,Multiplication,Division** were residing in one landing file which created tight coupling between components. If landing page goes down for whatever reason ,entire application becomes inaccessible.


```Monolithic Architecure -> Microservices Architecture  ```



* All the functions are made independent applications
* Each application has its own port
* Landing page requests operation through http get request
* These applications run on different containers
* Docker-compose brings all containers online

### Task 1
* solved value error by using default value in input field of html file
* handled division by zero error

### Task 2
* created separate Applications for each function
* Added more functions 

## High Level Directory structure
.
├── Docs
├── README.md
└── microservices

## Microservices Directory
.
├── Addition
│   ├── Dockerfile
│   └── app
├── Division
│   ├── Dockerfile
│   └── app
├── Equal
│   ├── Dockerfile
│   └── app
├── Exponent
│   ├── Dockerfile
│   └── app
├── Gcd
│   ├── Dockerfile
│   └── app
├── Greater
│   ├── Dockerfile
│   └── app
├── Lcm
│   ├── Dockerfile
│   └── app
├── Lesser
│   ├── Dockerfile
│   └── app
├── Modulo
│   ├── Dockerfile
│   └── app
├── Multiplication
│   ├── Dockerfile
│   └── app
├── Subtraction
│   ├── Dockerfile
│   └── app
├── docker-compose.yaml
└── landing
    ├── Dockerfile
    └── app



## Commands 
**docker-compose up -d** builds all images and starts services
**docker-compose down** stops all running processess


__________________________________________________________________________________

