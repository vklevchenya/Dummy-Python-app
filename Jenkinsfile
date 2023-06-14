pipeline {
    agent any
    options {
        skipDefaultCheckout()
        buildDiscarder( logRotator(numToKeepStr:'10') )
    }

    // Added trigger for execution of pipeline hourly
    triggers {
        cron('15 * * * *')
    }

    parameters {
        string(name: 'TESTS_SCOPE', defaultValue: 'system', description: 'Scope of tests to run')
        string(name: 'THREADS_COUNTER', defaultValue: '2', description: 'Number of threads to run in parallel')
        string(name: 'BRANCH', defaultValue: 'main', description: 'Branch to build')
    }

        stages {
        // stage('Checkout App') {
        //     steps {
        //         checkout([
        //                 $class: 'GitSCM',
        //                 branches: [[name: "*/${params.BRANCH}"]],
        //                 doGenerateSubmoduleConfigurations: false,
        //                 extensions: [
        //                     [$class: 'CloneOption', noTags: false, reference: '', shallow: false]
        //                 ]
        //         ])
        //     }
        // }

        // Execution of system tests on JOB_TARGET_HOST environment with using container_name pytest3 (custom build)
        stage('Run tests on target environment') {
            environment {
               TARGET_HOST = "${params.JOB_TARGET_HOST}"
            }
            steps {
                container('pytest3') {
                    catchError {
                        bat "pip install -r requirements.txt"
                        bat "pytest -n ${params.THREADS_COUNTER} -k '${params.TESTS_SCOPE}' --junitxml=out_report.xml"
                    }
                }
            }
        }

        // Clean-up test data
        // stage('Clean-up test data') {
        //     // environment {
        //     //    TARGET_HOST = "${params.JOB_TARGET_HOST}"
        //     // }
        //     // steps {
        //     //     container('pytest3') {
        //     //         //sh(script: "python3 test_data_cleanup.py", returnStdout: true)
        //     //     }
        //     // }
        // }
        // Process failures, remove artifacts and prepare data for Slack notification
        // stage('Finalize run') {
        //     // environment {
        //     //    TARGET_HOST = "${params.JOB_TARGET_HOST}"
        //     // }
        //     // steps {
        //     //     container('pytest3') {
        //     //         script {
        //     //             failed_tests_content = sh(script: "python3 post_processing.py", returnStdout: true).trim()
        //     //         }
        //     //     }
        //     // }
        // }
    }

        // Post-execution steps: store report and send Slack notification in case, if build is failed
    post {
        always {
            junit '**/*_report.xml'
        }
        // fixed {
        //     slackSend color: 'good',
        //     message: "Build is back to normal: ${env.JOB_NAME} " +
        //     "(in ${currentBuild.durationString}):\n" +
        //     ":jenkins:: ${env.BUILD_URL}\n",
        //     tokenCredentialId: 'slack-integration-token'
        // }
        // failure {
        //     slackSend color: 'danger',
        //     message: "Failure! :rotating_light: ${env.JOB_NAME} " +
        //     ":jenkins_angry:: ${env.BUILD_URL}\n" +
        //     "(in ${currentBuild.durationString}):\n" +
        //     "${failed_tests_content}\n",
        //     tokenCredentialId: 'slack-integration-token'
        // }
    }
}