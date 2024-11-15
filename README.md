
📚 Comparación de Diseño: Con y Sin DIP
Este repositorio presenta una comparación entre dos enfoques de diseño de software: uno que aplica el Principio de Inversión de Dependencias (DIP) y otro que no lo hace. El objetivo es entender cómo el uso de este principio mejora la flexibilidad, mantenibilidad y capacidad de prueba del código. 🚀

🌟 ¿Qué es el DIP?
El Principio de Inversión de Dependencias es uno de los principios SOLID. Su idea principal es que:

Las clases de alto nivel no deben depender de clases de bajo nivel. Ambas deben depender de abstracciones.
Las abstracciones no deben depender de los detalles. Los detalles deben depender de abstracciones.

🛠️ Estructura del proyecto
El proyecto está dividido en dos implementaciones:

🟢 Con DIP
Implementa una interfaz abstracta (ProveedorPublicaciones) para desacoplar la lógica principal de las implementaciones concretas.
Ejemplo flexible que facilita agregar nuevas fuentes de datos sin modificar el código existente.
🔴 Sin DIP
Las clases de alto nivel están acopladas directamente a implementaciones concretas.
Dificulta la escalabilidad y aumenta el costo de mantenimiento.
