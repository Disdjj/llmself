# -*-coding:utf-8 -*-
import enum


class Role(enum.Enum):
    """
    Enumeration of various role-playing personas for code prompting and assistance.
    Each role represents a different expertise area or perspective.
    """

    # ========== Programming Language Experts ==========
    PYTHON_EXPERT = "python_expert"
    JAVASCRIPT_EXPERT = "javascript_expert"
    JAVA_EXPERT = "java_expert"
    CSHARP_EXPERT = "csharp_expert"
    CPP_EXPERT = "cpp_expert"
    RUST_EXPERT = "rust_expert"
    GO_EXPERT = "go_expert"
    TYPESCRIPT_EXPERT = "typescript_expert"
    PHP_EXPERT = "php_expert"
    RUBY_EXPERT = "ruby_expert"
    SWIFT_EXPERT = "swift_expert"
    KOTLIN_EXPERT = "kotlin_expert"
    SCALA_EXPERT = "scala_expert"
    HASKELL_EXPERT = "haskell_expert"

    # ========== Web Development Specialists ==========
    FRONTEND_DEVELOPER = "frontend_developer"
    BACKEND_DEVELOPER = "backend_developer"
    FULLSTACK_DEVELOPER = "fullstack_developer"
    REACT_SPECIALIST = "react_specialist"
    VUE_SPECIALIST = "vue_specialist"
    ANGULAR_SPECIALIST = "angular_specialist"
    NODE_SPECIALIST = "node_specialist"

    # ========== System & Infrastructure ==========
    SYSTEM_ARCHITECT = "system_architect"
    CLOUD_ARCHITECT = "cloud_architect"
    DEVOPS_ENGINEER = "devops_engineer"
    SRE_ENGINEER = "sre_engineer"
    INFRASTRUCTURE_ENGINEER = "infrastructure_engineer"
    KUBERNETES_EXPERT = "kubernetes_expert"
    DOCKER_EXPERT = "docker_expert"
    AWS_EXPERT = "aws_expert"
    AZURE_EXPERT = "azure_expert"
    GCP_EXPERT = "gcp_expert"

    # ========== Database & Data ==========
    DATABASE_ARCHITECT = "database_architect"
    DATA_ENGINEER = "data_engineer"
    DATA_SCIENTIST = "data_scientist"
    DATA_ANALYST = "data_analyst"
    SQL_EXPERT = "sql_expert"
    NOSQL_EXPERT = "nosql_expert"

    # ========== AI & Machine Learning ==========
    AI_RESEARCHER = "ai_researcher"
    ML_ENGINEER = "ml_engineer"
    DEEP_LEARNING_EXPERT = "deep_learning_expert"
    NLP_SPECIALIST = "nlp_specialist"
    COMPUTER_VISION_EXPERT = "computer_vision_expert"
    MLOps_ENGINEER = "mlops_engineer"

    # ========== Security & Testing ==========
    SECURITY_EXPERT = "security_expert"
    CYBERSECURITY_ANALYST = "cybersecurity_analyst"
    PENETRATION_TESTER = "penetration_tester"
    QA_ENGINEER = "qa_engineer"
    TEST_AUTOMATION_EXPERT = "test_automation_expert"

    # ========== Mobile Development ==========
    MOBILE_DEVELOPER = "mobile_developer"
    IOS_DEVELOPER = "ios_developer"
    ANDROID_DEVELOPER = "android_developer"
    FLUTTER_DEVELOPER = "flutter_developer"
    REACT_NATIVE_DEVELOPER = "react_native_developer"

    # ========== Game Development ==========
    GAME_DEVELOPER = "game_developer"
    UNITY_DEVELOPER = "unity_developer"
    UNREAL_DEVELOPER = "unreal_developer"

    # ========== Specialized Domains ==========
    BLOCKCHAIN_DEVELOPER = "blockchain_developer"
    IOT_DEVELOPER = "iot_developer"
    EMBEDDED_SYSTEMS_ENGINEER = "embedded_systems_engineer"
    ROBOTICS_ENGINEER = "robotics_engineer"
    FINTECH_DEVELOPER = "fintech_developer"

    # ========== Management & Leadership ==========
    TECH_LEAD = "tech_lead"
    ENGINEERING_MANAGER = "engineering_manager"
    PRODUCT_MANAGER = "product_manager"
    PROJECT_MANAGER = "project_manager"
    SCRUM_MASTER = "scrum_master"

    # ========== Educational & Mentoring ==========
    CODING_MENTOR = "coding_mentor"
    TECHNICAL_INSTRUCTOR = "technical_instructor"
    PROGRAMMING_TUTOR = "programming_tutor"
    CODE_REVIEWER = "code_reviewer"

    # ========== Consulting & Advisory ==========
    TECHNICAL_CONSULTANT = "technical_consultant"
    SOLUTION_ARCHITECT = "solution_architect"
    PERFORMANCE_EXPERT = "performance_expert"
    CODE_OPTIMIZATION_EXPERT = "code_optimization_expert"

    # ========== General Purpose ==========
    SENIOR_DEVELOPER = "senior_developer"
    JUNIOR_DEVELOPER = "junior_developer"
    CODING_ASSISTANT = "coding_assistant"
    TECHNICAL_WRITER = "technical_writer"
    API_DESIGNER = "api_designer"

    # ========== Creative & Design ==========
    UI_UX_DEVELOPER = "ui_ux_developer"
    CREATIVE_TECHNOLOGIST = "creative_technologist"
